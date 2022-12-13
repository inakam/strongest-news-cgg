import React from 'react';

import CommentPostPanel from '../components/CommentPostPanel';
import CommentViewPanel from '../components/CommentViewPanel';
import NewsViewPanel from '../components/NewsViewPanel';

class NewsDetailView extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoaded: false,
      article: {
        title: '',
        img_url: '',
        detail: '',
        updated_at: null,
        type: '',
      },
      comments: [],
      commentForm: {
        name: '',
        message: '',
      },
    };
    this.onChangeNameHandler = this.onChangeNameHandler.bind(this);
    this.onChangeMessageHandler = this.onChangeMessageHandler.bind(this);
    this.onSubmitCommentHandler = this.onSubmitCommentHandler.bind(this);
  }
  componentDidMount() {
    const { params } = this.props.match;
    this.fetchArticle(params.id);
    this.fetchComments(params.id);
  }
  fetchArticle(articleId) {
    fetch(process.env.REACT_APP_BACKEND_API_ENDPOINT + `/articles/${articleId}`, {
      mode: 'cors',
    })
      .then((res) => res.json())
      .then(
        (json) => {
          console.log('article', json);
          console.log(json);
          this.setState({
            isLoaded: true,
            article: json,
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error,
          });
        }
      );
  }
  fetchComments(articleId) {
    fetch(process.env.REACT_APP_BACKEND_API_ENDPOINT + `/comments/${articleId}`)
      .then((res) => res.json())
      .then(
        (json) => {
          console.log('comments', json);
          this.setState({
            isLoaded: true,
            comments: json,
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error,
          });
        }
      );
  }
  postComment(articleId, name, message) {
    const requestOptions = {
      method: 'POST',
      headers: new Headers({ 'Content-Type': 'application/json' }),
      body: JSON.stringify({
        article_id: articleId,
        detail: message,
        name: name,
      }),
    };
    fetch(process.env.REACT_APP_BACKEND_API_ENDPOINT + '/comments', requestOptions)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  resetCommentForm() {
    this.setState({
      commentForm: {
        name: '',
        message: '',
      },
    });
  }
  onChangeNameHandler(event) {
    const name = event.target.value;
    this.setState({
      commentForm: {
        ...this.state.commentForm,
        name: name,
      },
    });
  }
  onChangeMessageHandler(event) {
    const message = event.target.value;
    this.setState({
      commentForm: {
        ...this.state.commentForm,
        message: message,
      },
    });
  }
  onSubmitCommentHandler(event) {
    event.preventDefault();
    const { id } = this.props.match.params;
    const { name, message } = this.state.commentForm;
    this.postComment(id, name, message);
    this.fetchComments(id);
    this.resetCommentForm();
  }
  render() {
    const { article, comments, commentForm } = this.state;
    return (
      <>
        <div className="row">
          <NewsViewPanel
            title={article.title}
            imgUrl={article.img_url}
            detail={article.detail}
            updatedAt={article.updated_at}
            type={article.type}
          />
        </div>
        <div className="row">
          <CommentViewPanel comments={comments} />
        </div>
        <div className="row">
          <CommentPostPanel
            name={commentForm.name}
            message={commentForm.message}
            onChangeName={this.onChangeNameHandler}
            onChangeMessage={this.onChangeMessageHandler}
            onSubmitComment={this.onSubmitCommentHandler}
          />
        </div>
      </>
    );
  }
}

export default NewsDetailView;
