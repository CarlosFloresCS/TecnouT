<template>
  <header class="login-header">
    <div class="grey">
      Don't have an account?<RouterLink to="/sign_up">Sign up</RouterLink>.
    </div>
    <RouterLink to="/"
      ><img
        class="logo"
        src="https://img.icons8.com/parakeet/48/000000/anubis.png"
    /></RouterLink>
  </header>
  <main class="login-container">
    <h1>Welcome Back</h1>
    <div class="formlogin" id="signin_form">
      <div class="board_box">
        <button class="btn-lg" type="button">
          <img
            src="https://img.icons8.com/color/20/000000/google-logo.png"
            alt="google"
            class="imgoogle"
          />
          Sign in with Google
        </button>
        <div class="or-login">
          <span>OR</span>
        </div>
        <form method="POST" class="form-group">
          <label for="email">Email address</label>
          <input
            :value="email"
            @input="onEmailInput"
            autofocus="autofocus"
            class="form-control"
            name="email"
            id="email"
            placeholder="you@email.com"
            required="required"
          />
          <label for="password">Password</label>
          <input
            type="password"
            :value="password"
            @input="onPasswordInput"
            class="form-control"
            name="password"
            id="password"
            placeholder="password"
            required="required"
          />
          <button @click="onSignIn" class="btn-gris">Sign in</button>
          <br /><br />
          <div v-if="success && loginAttempt" id="success">Success!</div>
          <div v-if="!success && loginAttempt" id="fail">
            Incorrect username or password
          </div>
        </form>
      </div>
    </div>
  </main>
</template>

<script>
import { RouterLink } from "vue-router";
export default {
  name: "LoginView",
  components: { RouterLink },
  data() {
    return {
      email: "",
      password: "",
      success: false,
      loginAttempt: false,
    };
  },
  methods: {
    onEmailInput(e) {
      this.loginAttempt = false;
      this.email = e.target.value;
    },
    onPasswordInput(e) {
      this.loginAttempt = false;
      this.password = e.target.value;
    },
    onSignIn() {
      console.log("hola");
      const url = "http://localhost:5000/login";
      const body = {
        email: this.email,
        password: this.password,
      };

      fetch(url, {
        method: "POST",
        body: JSON.stringify(body),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          this.loginAttempt = true;
          this.success = data.success;
        });
    },
  },
};
</script>

<style scoped>
.logo {
  margin-top: -30px;
}
#success {
  color: green;
}
#fail {
  color: red;
}

* {
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
}

.login-header {
  margin: 30px 0 40px;
  box-sizing: border-box;
}

.login-container {
  max-width: 400px;
  margin: 0 auto;
  font-size: 15px;
  text-align: center;
}

.login-container h1 {
  font-size: 24px;
  text-align: center;
  margin: 0 0 30px;
  font-weight: 600;
}

.grey {
  margin-left: 80vw;
}

.formlogin {
  box-sizing: border-box;
  display: block;
  margin-top: 0em;
  font-size: 15px;
  text-align: center;
}

.board_box {
  box-shadow: 0px 1px 2px rgb(0 0 0 / 5%);
  border: 1px solid var(--colors-grey-300);
  padding: 30px 28px 28px 28px;
  background-color: #fff;
  border-radius: 4px;
  margin-bottom: 30px;
  text-align: left;
  font-size: 14px;
}

span {
  position: relative;
  display: inline-block;
  text-align: center;
  font-size: 11px;
  font-weight: 700;
  color: var(--colors-grey-600);
  box-sizing: border-box;
}

.btn-lg {
  width: 100%;
  padding: 15px;
  display: inline-block;
  text-align: center;
  color: var(--colors-grey-900);
  background-color: #fff;
  font-size: 14px;
  line-height: 14px;
  font-weight: 500;
  border-radius: 3px;
  transition: all 250ms ease;
  box-shadow: 0px 1px 5px rgb(0 0 0 / 10%);
  border: 1px solid var(--colors-grey-300);
  vertical-align: baseline;
  height: 54px;
}

.imgoogle {
  text-align: center;
  font-size: 14px;
  line-height: 14px;
  font-weight: 500;
  display: inline-block;
  margin-right: 5px;
  vertical-align: middle;
  width: auto;
  margin-top: -1px !important;
}

.or-login {
  overflow: hidden;
  text-align: center;
  color: var(--colors-grey-600);
  margin: 16px 0;
  font-size: 11px;
  font-weight: 700;
}

.form-group {
  margin-bottom: 10px;
  line-height: 1.8em;
}

label {
  font-size: 15px;
  color: var(--colors-grey-1000);
  font-weight: 600;
  margin-bottom: 3px;
  display: inline-block;
  max-width: 100%;
  cursor: default;
}

.form-control {
  height: 30px;
  padding: 10px 12px;
  font-size: 15px;
}

input {
  box-shadow: none;
  border-radius: 3px;
  background-color: #fcfcfc;
  transition: all 250ms ease;
  line-height: 25px;
  writing-mode: horizontal-tb !important;
  text-rendering: auto;
  letter-spacing: normal;
  word-spacing: normal;
  text-transform: none;
  text-indent: 0px;
  text-shadow: none;
  text-align: start;
  appearance: auto;
  -webkit-rtl-ordering: logical;
  cursor: text;
}

button {
  width: 100%;
  padding: 15px;
  margin-top: 10px;
  font-size: 15px;
  height: 54px;
}

.btn-gris {
  background: #24252a;
  border-color: #24252a;
  color: #fff !important;
}
</style>
