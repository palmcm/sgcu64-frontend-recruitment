const form = document.getElementById("register-form")
form.addEventListener("submit", event => {
  event.preventDefault()
  const formData = new FormData(form)
  const data = {}
  console.log(form.children)
  for (const [key, value] of formData.entries()) {
    /* USER CODE Begin: Validate data */
    if (!value){
      alert("Please fill all field");
      return
    }
    data[key] = value
    /* USER CODE Begin: Validate data */
  }
  console.log(data)
  /* USER CODE Begin: What happened next after recieve form data (Optional) */
  let emailregex = /.+@.+/;
  if (!emailregex.test(data["email"])){
    alert("Email is not in correct form");
    return
  }
  if (data["password"] != data["confirmpassword"]){
    alert("Confirm password is not correct");
    return
  }
  /* USER CODE END: What happened next after recieve form data (Optional) */
})
