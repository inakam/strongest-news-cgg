import React from 'react';

const SideBar = () => (
  <div className="sidebar" data-color="white" data-active-color="danger">
    <div className="sidebar-wrapper">
      <ul className="nav">
        <li>
          <a href="/">
            <i className="nc-icon nc-bank"></i>
            <p>ニュース一覧</p>
          </a>
        </li>

        <li>
          <a href="/latest">
            <i className="nc-icon nc-watch-time"></i>
            <p>最新のニュース</p>
          </a>
        </li>
      </ul>
    </div>
  </div>
);

export default SideBar;
