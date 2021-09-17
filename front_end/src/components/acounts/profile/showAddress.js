import React, { Component } from "react";
import { Link } from "react-router-dom";

class ShowAddress extends Component {
  render() {
    return (
      <div>
        <p className="pt-3 mb-2 px-1">{this.props.address}</p>
        <Link
          to="/profile/address"
          className="ml-auto m-2 btn h-25 btn-outline-info btn-sm "
        >
            {this.props.address &&' ویرایش آدرس'}
            {!this.props.address &&'افزودن آدرس'}
        </Link>
      </div>
    );
  }
}

export default ShowAddress;
