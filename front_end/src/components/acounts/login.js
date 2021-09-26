import React, { Component } from "react";
import { Link, Redirect } from "react-router-dom";

class Login extends Component {
  state = { redirectToProfile: false };
  handleOnLogin = (e) => {
    e.preventDefault();
    const form = new FormData(e.target);
    fetch("http://127.0.0.1:8000/api/v1/customers/register_login", {
      method: "PUT",
      body: form,
    })
      .then((res) => res.json())
      //  in this part we will store access token in to session storage
      .then((res) => {
        if (res["token"]) {
          sessionStorage.setItem("token", "Token " + res.token);
          this.setState({ redirectToProfile: true });
        }
      });
  };
  redirectToProfile = () => {
    if (this.state.redirectToProfile) return <Redirect to="/profile" />;
  };

  render() {
    // if customer is already logged in it will redirect to profile page
    if (sessionStorage.getItem("token")) {
      this.setState({ redirectToProfile: true });
    }
    return (
      <div className="bg-light h-100vh pt-3">
        {/* if redirect is true it will call redirect function to redirect */}
        {this.state.redirectToProfile && this.redirectToProfile()}
        <div className="row m-0">
          <div className="d-flex flex-column  col-3 mx-auto bg-white shadow rounded">
            <i className="bi-person-circle mt-3 text-center display-2 text-success"></i>
            <h6 className="text-center">ورود به حساب کاربری</h6>
            <form
              onSubmit={this.handleOnLogin}
              dir="rtl"
              className="mt-3 text-right"
              action=""
            >
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
                <label className="small" htmlFor="password">
                  کلمه عبور
                </label>
                <input
                  className="form-control rounded-pill"
                  type="password"
                  name="password"
                  id="password"
                  placeholder="کلمه عبود خود را وارد کنید"
                />
              </div>

              <button className="btn btn-success w-100 mb-2 mt-3 rounded shadow">
                ورود به حساب
              </button>
            </form>

            <Link
              to="/reset_password_email"
              className="small text-muted text-center text-decoration-none nav-link py-3"
            >
              کلمه عبور خود را فراموش کردم
            </Link>

            <Link
              className="text-center text-decoration-none text-info mb-1"
              to="/register"
            >
              ایجاد حساب کاربری
            </Link>
          </div>
        </div>
      </div>
    );
  }
}

export default Login;
