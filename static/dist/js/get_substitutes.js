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
        postJsonData(ajax_url_save_substitutes, {
          "products": checkbox.value,
          "ref_product_id": ref_product_id,
          "status": true
        }, {
          "Accept": "application/json",
          "Content-Type": "application/json"
        })
        .then(jsonResponse => {
            let max_in_db_reached = jsonResponse.max_in_db_reached;
            if (max_in_db_reached == true) {
                let overlay = document.getElementById('warn-popup');
                checkbox.checked = false;
                overlay.style.visibility='visible';
                overlay.style.opacity=1;
            }
        })
      } else {
        postJsonData(ajax_url_delete_substitutes, {
          "products": checkbox.value,
          "ref_product_id": ref_product_id,
          "status": false
        }, {
          "Accept": "application/json",
          "Content-Type": "application/json"
        })
      }
    })
  });


let exit = document.querySelector(".exit")
exit.addEventListener("click", function(e) {
    let overlay = document.getElementById('warn-popup');
    overlay.style.visibility='hidden';
    overlay.style.opacity=0;
})


