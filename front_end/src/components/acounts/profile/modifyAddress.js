import React, { Component } from "react";

class ModifyAddress extends Component {
  state = {...this.props.address}
  render() {
    console.log( this.state)
    return (
      <div className="d-flex">
        <iframe
          className="w-100"
          src="https://maps.google.com/maps?q=%D9%85%DA%A9%D8%AA%D8%A8%20%D8%B4%D8%B1%DB%8C%D9%81&t=&z=15&ie=UTF8&iwloc=&output=embed"
          frameBorder="0"
          scrolling="no"
          marginHeight="0"
          marginWidth="0"
        />

        <form className="p-3 w-100" dir="rtl">
          <div className="form-group">
            <label htmlFor="street">خیابان</label>
            <input
              className="form-control w-100"
              type="text"
              name="street"
              id="street"
              placeholder="اسم خیابان"
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
            />
          </div>
          <div className="form-group">
            <label htmlFor="postal_code">کد پستی</label>
            <input
              className="form-control w-100"
              type="number"
              name="postal_code"
              id="postal_code"
              placeholder="کد پستی"
            />
          </div>
          <div className="form-group">
            <label htmlFor="number">پلاک</label>
            <input
              className="form-control w-100"
              type="number"
              name="number"
              id="number"
              placeholder="پلاک"
            />
          </div>
          <div className="form-group">
            <label htmlFor="dore_phone">زنگ</label>
            <input
              className="form-control w-100"
              type="number"
              name="dore_phone"
              id="dore_phone"
              placeholder="زنگ"
            />
          </div>
          <button className="btn btn-success">ویرایش آدرس</button>
        </form>
      </div>
    );
  }
}

export default ModifyAddress;
