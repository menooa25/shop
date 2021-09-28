const redirectToLogin = () => {
  window.location.assign("/login");
};
const CheckUserAuth = () => {
  // if user is not auth or token is expired it will redirect to /profile
  const token = sessionStorage.getItem("token");
  if (!token) {
    redirectToLogin();
  } else {
    const headers = new Headers();
    headers.set("Authorization", token);
    fetch("http://127.0.0.1:8000/api/v1/customers/check_user_auth", {
      method: "GET",
      headers,
    }).then((res) => {
      if (res.status === 401) redirectToLogin();
      else return true;
    });
  }
};
export default CheckUserAuth;
