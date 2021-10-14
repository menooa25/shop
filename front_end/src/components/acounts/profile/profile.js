import React, { Component } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import ShowAddress from "./showAddress";
import ModifyAddress from "./modifyAddress";
import CheckoutsHistory from "./checkoutsHistory";
import DeliveredCheckoutHistory from "./deliveredCheckoutHistory";
import CheckUserAuth from "../../../utils/checkUserAuth";
import SiteURL from "../../../utils/url";

class Profile extends Component {
  state = {
    username: "",
    first_name: "",
    last_name: "",
    phone: "",
    address_str: "",
    address: null,
  };

  render() {
    // CheckUserAuth();
    return (
      <div className="h-100vh bg-light">
        <div className="container">
          <div className="row m-0">
            <div className="col-8 h-100vh">
              <div className="row m-0 mt-3 text-info" dir="rtl">
                <h4>
                  <i className="bi bi-dot icons" />
                  آدرس من
                </h4>
              </div>
              {/* after here is customer address */}
              <BrowserRouter>
                <div className="rounded bg-white shadow text-right mr-3">
                  <Switch>
                    <Route path="/profile/address">
                      <ModifyAddress address={this.state.address} />
                    </Route>
                    <Route path="/profile">
                      <ShowAddress address={this.state.address_str} />
                    </Route>
                  </Switch>
                </div>
              </BrowserRouter>
              {/* after here delivered checkouts history will be shown */}
              <div className="row m-0 mt-3 text-info" dir="rtl">
                <h4>
                  <i className="bi bi-dot icons" />
                  سفارشات تهویل داده نشده
                </h4>
              </div>
              <DeliveredCheckoutHistory />
              {/* after here checkout history will be shown */}
              <div className="row m-0 mt-3 text-info" dir="rtl">
                <h4>
                  <i className="bi bi-dot icons" />
                  سفارشات من
                </h4>
              </div>

              <CheckoutsHistory />
            </div>

            {/* after here profile info will be shown */}
            <div className="col-4 h-100vh">
              <div className="rounded mt-3 shadow bg-white">
                <h4 className="text-center mb-0 pt-2">ویرایش اطلاعات</h4>
                <form
                  onSubmit={this.handleOnUpdate}
                  dir="rtl"
                  className="rounded "
                  action=""
                >
                  <div className="d-flex flex-column p-2 text-right">
                    <div className="form-group">
                      <label className="small" htmlFor="first_name">
                        نام
                      </label>
                      <input
                        onChange={this.handleOnChange}
                        className="form-control rounded-pill"
                        type="text"
                        name="first_name"
                        id="first_name"
                        placeholder="نام خود را وارد کنید"
                        value={this.state.first_name}
                        required
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
                        value={this.state.last_name}
                        onChange={this.handleOnChange}
                        required
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
                        value={this.state.username}
                        onChange={this.handleOnChange}
                        required
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
                        value={this.state.phone}
                        onChange={this.handleOnChange}
                      />
                    </div>
                  </div>
                  <div className="px-2">
                    <button className="btn btn-success w-100 my-2 rounded shadow">
                      بروزرسانی اطلاعات
                    </button>
                  </div>
                </form>
              </div>
              <div className="rounded shadow bg-white mt-4">
                <h4 className="text-center mb-0 pt-2">تغیر رمز عبور</h4>

                {/* change password part */}
                <form
                  onSubmit={this.handleOnChangePassword}
                  className="px-2 text-right"
                >
                  <div className="form-group">
                    <label className="small" htmlFor="password">
                      کلمه عبور
                    </label>
                    <input
                      className="form-control rounded-pill text-right"
                      type="password"
                      name="password"
                      id="password"
                      placeholder="کلمه عبود خود را وارد کنید"
                    />
                  </div>
                  <div className="form-group">
                    <label className="small" htmlFor="password1">
                      کلمه عبور جدید
                    </label>
                    <input
                      className="form-control rounded-pill text-right"
                      type="password"
                      name="password1"
                      id="password1"
                      placeholder="کلمه عبود جدید خود را وارد کنید"
                    />
                  </div>
                  <div className="form-group">
                    <label className="small" htmlFor="password2">
                      تایید کلمه عبور جدید
                    </label>
                    <input
                      className="form-control rounded-pill text-right"
                      type="password"
                      name="password2"
                      id="password2"
                      placeholder="کلمه عبور جدید خود را مجددن  وارد کنید"
                    />
                  </div>
                  <button className="btn btn-danger w-100 mb-2 mt-2 rounded shadow">
                    تغیر رمز عبور
                  </button>
                </form>
                {/* end of change password part */}
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  handleOnChangePassword = (e) => {
    e.preventDefault();
    const form = new FormData(e.target);
    const header = new Headers();
    const token = sessionStorage["token"];
    header.set("Authorization", token);
    fetch(SiteURL + "/api/v1/customers/customer_change_password", {
      method: "POST",
      body: form,
      headers: header,
    });
  };

  handleOnUpdate = (e) => {
    // we are updating customer info here
    e.preventDefault();
    const form = new FormData(e.target);
    const header = new Headers();
    const token = sessionStorage["token"];
    header.set("Authorization", token);
    fetch(SiteURL + "/api/v1/customers/customer_profile", {
      method: "PUT",
      body: form,
      headers: header,
    });
  };
  handleOnChange = (e) => {
    const element = e.target;
    let element_state = {};
    element_state[element.name] = element.value;
    this.setState(element_state);
  };

  componentDidMount() {
    const header = new Headers();
    const token = sessionStorage["token"];
    // getting customer profile info from token and storing
    header.set("Authorization", token);
    fetch(SiteURL + "/api/v1/customers/customer_profile", {
      method: "GET",
      headers: header,
    })
      .then((res) => res.json())
      .then((res) => this.setState(res));
  }
}

export default Profile;
