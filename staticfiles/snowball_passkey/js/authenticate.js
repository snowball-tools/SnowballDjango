<<<<<<< HEAD
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

fetch("passkey/begin_authentication/")
=======
fetch("/begin_registration/")
>>>>>>> a8b9195 (hmmm)
  .then((response) => response.json())
  .then((data) => {
    const publicKey = {
      challenge: Uint8Array.from(window.atob(data.challenge), (c) =>
        c.charCodeAt(0)
      ),
<<<<<<< HEAD
      allowCredentials: [
        {
          type: "public-key",
          id: Uint8Array.from(window.atob(data.credential_id), (c) =>
            c.charCodeAt(0)
          ),
        },
      ],
    };

    return navigator.credentials.get({ publicKey });
  })
  .then((assertion) => {
    const csrfToken = getCookie("csrftoken");

    fetch("passkey/finish_authentication/", {
      method: "POST",
      body: JSON.stringify(assertion),
      headers: {
        "X-CSRFToken": csrfToken,
        "Content-Type": "application/json",
      },
=======
      rp: { name: "Your Website Name" },
      user: {
        id: Uint8Array.from(window.atob(data.username), (c) => c.charCodeAt(0)),
        name: data.username,
        displayName: data.username,
      },
      pubKeyCredParams: [{ type: "public-key", alg: -7 }],
      authenticatorSelection: { authenticatorAttachment: "platform" },
    };

    return navigator.credentials.create({ publicKey });
  })
  .then((credential) => {
    fetch("/finish_registration/", {
      method: "POST",
      body: JSON.stringify(credential),
>>>>>>> a8b9195 (hmmm)
    });
  });
