import React, { Component } from "react";
import SiteURL from "../../../utils/url";

class ModifyAddress extends Component {
  state = {
    street: "",
    alley: "",
    postal_code: "",
    number: "",
    dore_phone: "",
  };

  render() {
    return (
      <div className="d-flex">
        <iframe
          className="w-100"
          src="https://maps.google.com/maps?q=%D9%85%DA%A9%D8%AA%D8%A8%20%D8%B4%D8%B1%DB%8C%D9%81&t=&z=15&ie=UTF8&iwloc=&output=embed"
          frameBorder="0"
          scrolling="no"
          marginHeight="0"
          marginWidth="0"
          title="google map"
        />

        <form className="p-3 w-100" dir="rtl" onSubmit={this.handleOnSubmit}>
          <div className="form-group">
            <label htmlFor="street">خیابان</label>
            <input
              className="form-control w-100"
              type="text"
              name="street"
              id="street"
              placeholder="اسم خیابان"
              value={this.state.street}
              onChange={this.handleOnChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="alley">کوچه</label>
            <input
              className="form-control w-100"
              type="text"
              name="alley"
              id="alley"
              placeholder="اسم کوچه"
              value={this.state.alley}
              onChange={this.handleOnChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="postal_code">کد پستی</label>
            <input
              className="form-control w-100"
              type="tell"
              name="postal_code"
              id="postal_code"
              placeholder="کد پستی"
              value={this.state.postal_code}
              onChange={this.handleOnChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="number">پلاک</label>
            <input
              className="form-control w-100"
              type="tell"
              name="number"
              id="number"
              placeholder="پلاک"
              value={this.state.number}
              onChange={this.handleOnChange}
            />
          </div>
          <div className="form-group">
            <label htmlFor="dore_phone">زنگ</label>
            <input
              className="form-control w-100"
              type="tell"
              name="dore_phone"
              id="dore_phone"
              placeholder="زنگ"
              value={this.state.dore_phone}
              onChange={this.handleOnChange}
            />
          </div>
          <button className="btn btn-success">ویرایش آدرس</button>
        </form>
      </div>
    );
  }

  handleOnChange = (e) => {
    const element = e.target;
    let address_state = {};
    address_state[element.name] = element.value;
    this.setState(address_state);
  };

  handleOnSubmit = (e) => {
    e.preventDefault();
    const form = new FormData(e.target);
    const header = new Headers();
    const token = sessionStorage["token"];
    header.set("Authorization", token);
    fetch(SiteURL + "/api/v1/customers/customer_address", {
      method: "PUT",
      body: form,
      headers: header,
    }).then(() => {
      sessionStorage.clear();
      window.location.assign("/login");
    });
  };
  // here we will fill the customer address data
  fillStateWithAddress = () => {
    if (this.state.street == "" && this.props.address) {
      this.setState({
        street: this.props.address[1],
        alley: this.props.address[2],
        postal_code: this.props.address[3],
        number: this.props.address[4],
        dore_phone: this.props.address[5],
      });
    }
  };

  componentDidMount() {
    // we are little waiting till data will be ready
    setTimeout(this.fillStateWithAddress, 300);
  }
}

export default ModifyAddress;
