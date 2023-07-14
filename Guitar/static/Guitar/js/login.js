form.addEventListener("submit", e => {
    let warnings = "";
    let entrar = true;
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  
    if (user.value.length < 6) {
      warnings += "Nombre de usuario inválido <br>";
      entrar = false;
    }
  
    if (!regexEmail.test(email.value)) {
      warnings += "Email inválido <br>";
      entrar = false;
    }
  
    if (pass.value.length <= 8) {
      warnings += "Contraseña inválida <br>";
      entrar = false;
    }
  
    parrafo.innerHTML = warnings;
  
    if (!entrar) {
      e.preventDefault(); // Evitar que el formulario se envíe si hay errores
    }
  });