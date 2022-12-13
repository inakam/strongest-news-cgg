import React from 'react';

import NewsPanel from '../components/NewsPanel';

class NewsAllView extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoaded: false,
      items: [],
    };
  }
  componentDidMount() {
    fetch(process.env.REACT_APP_BACKEND_API_ENDPOINT + '/titles', {
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

export default NewsAllView;
