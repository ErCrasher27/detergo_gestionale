<template>
  <div id="wrapper">
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <router-link to="/home" class="navbar-item">
          <a class="navbar-item">
            <img src="./assets/logo-detergo-svg.svg" width="117" height="67">
          </a>
        </router-link>

        <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <button class="button is-medium">
                <span class="icon">
                  <i class="fa-solid fa-gear"></i>
                </span>
              </button>

              <button class="button is-medium">
                <span class="icon">
                  <i class="fa-solid fa-right-from-bracket"></i>
                </span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view />
    </section>

    <footer class="footer">
      <div class="content has-text-centered">
        <p>
          <strong>Detergo Gestionale</strong> by <a href="">mini dev team</a>. The source code is licensed
          <a href="http://opensource.org/licenses/mit-license.php">MIT</a>. The website content
          is licensed <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY NC SA 4.0</a>.
        </p>
      </div>
    </footer>

  </div>
</template>

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

@font-face {
  font-family: "Gunterz";
  src: local("Gunterz"),
    url(./fonts/Fontspring-DEMO-gunterz-medium.otf) format("truetype");
}

.navbar .navbar-brand .navbar-item img {
  max-height: none;
}

.navbar .navbar-end .navbar-item .buttons .button.is-medium {
  background: #005C9D;
}

.navbar .navbar-menu .navbar-end .navbar-item .buttons .button.is-medium .icon i {
  color: #FFFFFF;
}

#wrapper .section {
  background: #004A7E;
}
</style>
