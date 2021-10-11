/*
save and/or remove substitute from results page.
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
  
  let ckbx = document.querySelectorAll("input[type=checkbox][name=product]");
  
  ckbx.forEach(function(checkbox) {
    checkbox.addEventListener("change", function(e) {
      e.preventDefault();
      if (checkbox.checked == true) {
        postJsonData(ajax_url, {
          "products": checkbox.value,
          "ref_product_id": ref_product_id,
          "status": "save"
        }, {
          "Accept": "application/json",
          "Content-Type": "application/json"
        })
      } else {
        postJsonData(ajax_url, {
          "products": checkbox.value,
          "ref_product_id": ref_product_id,
          "status": ""
        }, {
          "Accept": "application/json",
          "Content-Type": "application/json"
        })
      }
    })
  });


