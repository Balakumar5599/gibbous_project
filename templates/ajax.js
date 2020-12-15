const ENDPOINT = "http://w.localhost:8000/tenant";

function getUsers() {
  return fetch(ENDPOINT)
    .then(response => {
      if (!response.ok) throw Error(response.statusText);
      return response.json();
    })
    .then(json => json);
}

module.exports = { getUsers };