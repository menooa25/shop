import React, { Component } from "react";

class ResetPassword extends Component {
  changePassword = (e) => {
    e.preventDefault();
    const form = new FormData(e.target);
    fetch("http://127.0.0.1:8000/api/v1/customers/reset_password", {
      method: "PUT",
      body: form,
    });
  };
  render() {
    return (
      <div className="bg-light pt-4 h-100vh">
        <div className="row m-0">
          <div className="col-3 bg-white mx-auto rounded shadow d-flex flex-column">
            <i className="bi-shield-lock-fill mt-3 text-center display-2 text-success"></i>
            <h6 className="text-center">تغییر رمز عبور</h6>
            <form
              onSubmit={this.changePassword}
              dir="rtl"
              className="text-right mt-2"
            >
              <div className="form-group">
                <label htmlFor="code">
                  کد تعیید
                  <span>( این کد برای شما ایمیل شده )</span>
                </label>
                <input
                  type="text"
                  id="code"
                  name="code"
                  className="form-control"
                />
              </div>
              <div className="form-group">
                <label htmlFor="password1">رمز جدید</label>
                <input
                  type="password"
                  id="password1"
                  name="password1"
                  className="form-control"
                />
              </div>
              <div className="form-group">
                <label htmlFor="password2">تکرار رمز جدید</label>
                <input
                  type="password"
                  id="password2"
                  name="password2"
                  className="form-control"
                />
              </div>
              <button className="btn btn-info form-control mb-3">
                تغییر رمز
              </button>
            </form>
          </div>
        </div>
      </div>
    );
  }
}

export default ResetPassword;
