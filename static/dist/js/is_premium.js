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
        }, {
            once: true
        });
    });
