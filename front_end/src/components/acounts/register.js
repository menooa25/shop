import React, { Component } from "react";

class Register extends Component {
  handleOnRegister = (e) => {
    e.preventDefault();
    const form = new FormData(e.target);
    fetch("http://127.0.0.1:8000/api/v1/customers/register_login", {
      method:'POST',
      body: form,
    })
      .then((res) => res.json())
      //  In this part we will get errors and it will shown to user
      .then((res) => res);
  };

  render() {
    return (
      <div className="bg-light w-100vh pt-3">
        <div className="row m-0">
          <div className="d-flex flex-column  col-5 mx-auto bg-white shadow rounded">
            <i className="bi-person-plus-fill mt-3 text-center display-2 text-success"></i>
            <h6 className="text-center">حساب کاربری جدید بسازید</h6>
            <form
              onSubmit={this.handleOnRegister}
              dir="rtl"
              className="mt-3"
              action=""
            >
              <div className="d-flex text-right">
                <div className="px-1 w-100">
                  <div className="form-group">
                    <label className="small" htmlFor="first_name">
                      نام
                    </label>
                    <input
                      className="form-control rounded-pill"
                      type="text"
                      name="first_name"
                      id="first_name"
                      placeholder="نام خود را وارد کنید"
                    />
                  </div>
                  <div className="form-group">
                    <label className="small" htmlFor="last_name">
                      نام خانوادگی
                    </label>
                    <input
                      className="form-control rounded-pill"
                      type="text"
                      name="last_name"
                      id="last_name"
                      placeholder="نام خانوادگی خود را وارد کنید"
                    />
                  </div>
                  <div className="form-group">
                    <label className="small" htmlFor="password1">
                      کلمه عبور
                    </label>
                    <input
                      className="form-control rounded-pill"
                      type="password"
                      name="password1"
                      id="password1"
                      placeholder="کلمه عبود خود را وارد کنید"
                    />
                  </div>
                </div>
                <div className="px-1 w-100">
                  <div className="form-group">
                    <label className="small" htmlFor="email">
                      آدرس ایمیل
                    </label>
                    <input
                      className="form-control rounded-pill"
                      type="email"
                      name="username"
                      id="email"
                      placeholder="ایمیل خود را وارد کنید"
                    />
                  </div>
                  <div className="form-group">
                    <label className="small" htmlFor="phone">
                      شماره موبایل
                    </label>
                    <input
                      className="form-control rounded-pill"
                      type="tell"
                      name="phone"
                      id="phone"
                      placeholder="شماره موبایل خود را وارد کنید"
                      required
                    />
                  </div>
                  <div className="form-group">
                    <label className="small" htmlFor="password2">
                      تایید کلمه عبور
                    </label>
                    <input
                      className="form-control rounded-pill"
                      type="password"
                      name="password2"
                      id="password2"
                      placeholder="کلمه عبور خود را مجددن  وارد کنید"
                    />
                  </div>
                </div>
              </div>
              <button className="btn btn-success w-100 mb-2 mt-3 rounded shadow">
                ایجاد حساب کاربری
              </button>
            </form>
            <span className="small text-muted text-center py-3">
              با عضویت در اسم فروشگاه شما با <b>قوانین و مقررات</b> ما موافقت
              می‌کنید
            </span>
          </div>
        </div>
      </div>
    );
  }
}

export default Register;
