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
                  "product_id": checkbox.value,
                  "reference_id": reference_id,
              }, {
                  "Accept": "application/json",
                  "Content-Type": "application/json",
                  "X-CSRFToken": csrftoken
              })
              .then(jsonResponse => {
                  let is_max_in_db_reached = jsonResponse.is_max_in_db_reached;
                  if (is_max_in_db_reached == true) {
                      let overlay = document.getElementById('warn-popup');
                      checkbox.checked = false;
                      overlay.style.visibility = 'visible';
                      overlay.style.opacity = 1;
                  }
              })
      } else {
          postJsonData(ajax_url_delete_substitutes, {
              "product_id": checkbox.value,
              "reference_id": reference_id,
          }, {
              "Accept": "application/json",
              "Content-Type": "application/json",
              "X-CSRFToken": csrftoken
          })
      }
  })
});


let exit = document.querySelector(".exit")
exit.addEventListener("click", function(e) {
  let overlay = document.getElementById('warn-popup');
  overlay.style.visibility = 'hidden';
  overlay.style.opacity = 0;
})