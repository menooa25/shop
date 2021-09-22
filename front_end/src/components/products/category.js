import React, { Component } from "react";

class Category extends Component {
  state = { address: null };

  render() {
    return (
      <div className="d-flex justify-content-end rounded shadow mt-2 bg-white p-2 ">
        {/* passing back category id for filter by category */}
        {this.state.address &&
          this.state.address.map((category) => {
            return (
              <button
                className="btn text-secondary"
                key={category.id}
                id={category.id}
                onClick={() => this.props.value(category.id)}
              >
                {category.name}
              </button>
            );
          })}
        <button
          className="btn text-secondary"
          onClick={() => this.props.value(-1)}
        >
          همه
        </button>
      </div>
    );
  }

  //  getting category list
  componentDidMount() {
    fetch("http://127.0.0.1:8000/api/v1/products/categories")
      .then((res) => res.json())
      .then((res) => this.setState({ address: res }));
  }
}

export default Category;
