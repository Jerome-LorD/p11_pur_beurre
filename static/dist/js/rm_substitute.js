/*
Remove substitute from favorite page.
*/

async function postJsonData(url, data, headers) {
    try {
      const response = await fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: headers
      });
      return await response.json();
  
    } catch (err) {
      return console.warn(err);
    }
  }
  
  buttons = document.querySelectorAll(".btn-outline-warning")
    .forEach((button) => {
      button.addEventListener("click", (event) => {
        let prodbox = document.getElementById("fav-" + event.target.value);
        prodbox.parentNode.removeChild(prodbox);
  
        postJsonData(ajax_url_delete_substitutes, {
            "products": event.target.value,
            "ref_product_id": "",
            "status": false
          }, {
            "Accept": "application/json",
            "Content-Type": "application/json"
          })
          .then(jsonResponse => {
            let reference_id = jsonResponse.reference_id;
            postJsonData(ajax_url_delete_substitutes, {
              "products": event.target.value,
              "ref_product_id": reference_id,
              "status": false
            }, {
              "Accept": "application/json",
              "Content-Type": "application/json"
            })
          })
      });
    });
