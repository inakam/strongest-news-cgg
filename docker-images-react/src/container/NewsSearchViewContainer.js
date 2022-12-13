import React from 'react';
import queryString from 'query-string';

import NewsPanel from '../components/NewsPanel';

class NewsSearchView extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoaded: false,
      items: [],
    };
  }
  componentDidMount() {
    const values = queryString.parse(this.props.location.search);
    fetch(process.env.REACT_APP_BACKEND_API_ENDPOINT + `/keywords?keyword=${values.keyword}`, {
      mode: 'cors',
    })
      .then((res) => res.json())
      .then(
        (json) => {
          console.log(json);
          this.setState({
            isLoaded: true,
            items: json,
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
  render() {
    return (
      <div className="row">
        {this.state.items.map((item) => (
          <NewsPanel title={item.title} imgUrl={item.img_url} articleId={item.id} key={item.id} />
        ))}
      </div>
    );
  }
}

export default NewsSearchView;
