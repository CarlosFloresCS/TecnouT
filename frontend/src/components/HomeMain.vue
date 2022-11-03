<template>
  <div class="main">
    <section class="hero">
      <div class="left-column">
        <h1>TecnouT</h1>
        <h4>
          A virtual espace to<br />
          enjoy your studies
        </h4>
        <div class="btn">
          <RouterLink to="/sign_in">
            <button type="button" class="login-btn">Sig in</button>
          </RouterLink>
          <RouterLink to="/sign_up">
            <button type="button" class="login-btn">Sign up</button>
          </RouterLink>
        </div>
      </div>
      <div class="right-column">
        <img src="../../dist/img/inicio.png" />
      </div>
    </section>
  </div>
</template>

<script>
import { RouterLink } from "vue-router";
// @ is an alias to /src
export default {
  name: "HomeView",
  components: { RouterLink },
};
</script>

<style lang="scss" scoped>
.btn {
  align-items: center;
}

.btn button {
  padding: 15px 50px;
  margin-top: 50px;
  margin-left: 300px;
  outline: none;
  border: 1px solid #313446;
  border-radius: 20px;
  cursor: pointer;
  color: #c1c2cc;
  background: transparent;
  text-align: justify;
}

.btn .login-btn {
  background: linear-gradient(#16131ccc, #4d3877cc);
  box-shadow: 0 2px 15px rgba(232, 226, 228, 0.26);
  color: #fff;
}

.left-column,
.right-column {
  flex-basis: 50%;
}

.right-column img {
  width: 100%;
  margin-top: 200px;
}

.hero {
  background-image: url("../../dist/img/hero-bg.png");
  background-attachment: fixed;
  position: relative;
  height: 100vh;
  display: flex;

  img {
    object-fit: cover;
    width: 100%;
  }

  .left-column {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: #fff;

    h4 {
      margin-top: 50px;
      margin-left: 490px;
      text-transform: uppercase;
      font-size: 20px;
      padding-bottom: 4px;
    }

    h1 {
      margin-top: -30px;
      margin-left: 450px;
      font-size: 60px;
      @media (min-width: 550px) {
        font-size: 80px;
      }
    }

    hr:nth-child(2) {
      max-width: 365px;
      margin-bottom: 16px;
    }
    hr:nth-child(4) {
      height: 6px;
      background-color: #fff;
      border: none;
      max-width: 85px;
      margin-top: 16px;
    }
  }
}
</style>
