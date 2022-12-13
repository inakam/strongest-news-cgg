import React from 'react';

const CommentPostPanel = (props) => (
  <div id="comment-form" className="col-md-12">
    <div className="card card-user">
      <div className="card-header">
        <h4 className="card-title">コメントを投稿する</h4>
      </div>
      <div className="card-body">
        <form onSubmit={props.onSubmitComment}>
          <div className="row">
            <div className="col-md-3">
              <div className="form-group">
                <label>お名前</label>
                <input
                  type="text"
                  name="name"
                  className="form-control"
                  value={props.name}
                  onChange={props.onChangeName}
                />
              </div>
            </div>
          </div>

          <div className="row">
            <div className="col-md-12">
              <div className="form-group">
                <label>メッセージ</label>
                <textarea
                  name="detail"
                  className="form-control textarea"
                  value={props.message}
                  onChange={props.onChangeMessage}
                ></textarea>
              </div>
            </div>
          </div>

          <div className="row">
            <div className="update ml-auto mr-auto">
              <button type="submit" className="btn btn-primary btn-round">
                投稿する
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
);

export default CommentPostPanel;
