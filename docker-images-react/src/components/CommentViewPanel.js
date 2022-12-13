import React from 'react';

const CommentViewPanel = (props) => (
  <div id="comment" className="col-md-12">
    <div className="card">
      <div className="card-header">
        <h4 className="card-title">コメント</h4>
      </div>
      <div className="card-body">
        <div className="table-responsive">
          <table className="table">
            <thead className="text-primary">
              <tr>
                <th>ユーザー</th>
                <th>コメント</th>
              </tr>
            </thead>
            <tbody>
              {props.comments.map((comment) => (
                <tr key={comment.id}>
                  <td>{comment.name}</td>
                  <td>{comment.detail}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
);

export default CommentViewPanel;
