import React from 'react';

const NavBar = () => (
  <nav className="navbar navbar-expand-lg navbar-absolute fixed-top navbar-transparent">
    <div className="container-fluid">
      <div className="navbar-wrapper">
        <div className="navbar-toggle">
          <button type="button" className="navbar-toggler">
            <span className="navbar-toggler-bar bar1"></span>
            <span className="navbar-toggler-bar bar2"></span>
            <span className="navbar-toggler-bar bar3"></span>
          </button>
        </div>
        <a className="navbar-brand" href="/">
          最強ニュースサイト
        </a>
      </div>

      <button
        className="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navigation"
        aria-controls="navigation-index"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span className="navbar-toggler-bar navbar-kebab"></span>
        <span className="navbar-toggler-bar navbar-kebab"></span>
        <span className="navbar-toggler-bar navbar-kebab"></span>
      </button>

      <div className="collapse navbar-collapse justify-content-end" id="navigation">
        <form action="/search" method="GET">
          <div className="input-group no-border">
            <input
              type="text"
              name="keyword"
              className="form-control"
              placeholder="検索キーワード"
            />
            <button
              type="submit"
              style={{
                backgroundColor: 'transparent',
                border: 'none',
                cursor: 'pointer',
                outline: 'none',
                padding: 0,
                appearance: 'none',
              }}
            >
              <div className="input-group-text">
                <i className="nc-icon nc-zoom-split"></i>
              </div>
            </button>
          </div>
        </form>
      </div>
    </div>
  </nav>
);

export default NavBar;
