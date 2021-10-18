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

  gift_btn = document.querySelectorAll("#gift")
  .forEach((btn) => {
    btn.addEventListener("click", (event) => {
        let btn_confirm = document.createElement("button");
        let btn_txt = "Je confirme et valide mon don de 1€";
        btn_confirm.className = "gift-confirm btn-lg btn-success";
        btn_confirm.id = "confirm";
        btn_confirm.name = "gift";
        let btn_confirmContent = document.createTextNode(btn_txt);
        btn_confirm.appendChild(btn_confirmContent);
        document.querySelector("#gift-proposed").appendChild(btn_confirm);
    }, {once: true});
  });
  
  function hasClass(elem, className) {
    return elem.className.split(' ').indexOf(className) > -1;
}

document.addEventListener('click', function (e) {
    if (hasClass(e.target, 'gift-confirm')) {
        postJsonData(ajax_url_premium, {
            "is_premium": true,
            }, {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
            })
        let h3 = document.createElement("h3");
        let h3_text = "Merci " + current_user + ", nous vous avons envoyé un mail de confirmation à " + email_current_user;
        let h3Content = document.createTextNode(h3_text);
        h3.appendChild(h3Content);
        document.querySelector("#prem").appendChild(h3);
    }
}, {once: true});



