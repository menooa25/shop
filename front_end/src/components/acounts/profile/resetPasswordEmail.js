import React, { Component } from "react";
import { Link } from "react-router-dom";

class ResetPasswordEmail extends Component {
  createResetPasswordCode = (e) => {
    e.preventDefault();
    const form = new FormData(e.target);
    fetch("http://127.0.0.1:8000/api/v1/customers/reset_password", {
      method: "POST",
      body: form,
    });
    window.location.assign("/reset_password");
  };

  render() {
    return (
      <div className="bg-light pt-3 h-100vh">
        <div className="row">
          <div className="col-4 mx-auto bg-white rounded shadow ">
            <form
              onSubmit={this.createResetPasswordCode}
              className="m-2 text-right"
            >
              <div className="form-group">
                <label htmlFor="email">ایمیل</label>
                <input
                  className="form-control"
                  type="email"
                  id="email"
                  name="email"
                />
              </div>

              <button type="submit" className="btn btn-info form-control">
                رمز عبور را فراموش کردم
              </button>
            </form>
          </div>
        </div>
      </div>
    );
  }
}

export default ResetPasswordEmail;
