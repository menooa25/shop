import React, { Component } from "react";

class Profile extends Component {
  render() {
    return (
      <div className="h-100vh bg-light">
        <div className="container">
          <div className="row m-0">
            <div className="col-8 h-100vh"></div>
            <div className="col-4 h-100vh">
              <div className="rounded shadow">
                <form
                  onSubmit={this.handleOnRegister}
                  dir="rtl"
                  className="mt-3 rounded bg-white"
                  action=""
                >
                  <div className="d-flex flex-column p-2 text-right">
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
                  <div className='px-2'>
                    <button className="btn btn-success w-100 mb-2 mt-3 rounded shadow">
                    ایجاد حساب کاربری
                  </button>
                  </div>

                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Profile;
