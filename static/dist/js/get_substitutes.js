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
          "status": true
        }, {
          "Accept": "application/json",
          "Content-Type": "application/json"
        })
        .then(jsonResponse => {
            let max_in_db_reached = jsonResponse.max_in_db_reached;
            console.log("MAX", max_in_db_reached);
            if (max_in_db_reached == true) {
                let overlay = document.getElementById('warn-popup');
                // document.querySelector("input[type=checkbox][value=checkbox.value]").click();
                // ckbx_reverse.click();

                // let warn = "Vous avez atteint le nombre maximum de substituts en favoris.";
                // let p_warn = document.createElement("p");
                // p_warn.className = "warn-reached";
                // let p_warnContent = document.createTextNode(warn);
                // p_warn.appendChild(p_warnContent);
                // document.querySelector("#reached").appendChild(p_warn);
                overlay.style.visibility='visible';
                overlay.style.opacity=1;
                for(ckbx_reverse in document.querySelector("input[type=checkbox][value="+checkbox.value+"]")) {
                    console.log("base", ckbx_reverse.value);
                    if(ckbx_reverse.value == checkbox.value) {
                        // document.getElementsByClassName("product").click();
                        console.log(ckbx_reverse.value);
                    }
                 }
                
                // document.querySelector("input[type=checkbox][value="+checkbox.value+"]").click();
                // console.log(document.getElementsByClassName("product"));
            }
        })
      } else {
        postJsonData(ajax_url, {
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


