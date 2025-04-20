<script setup></script>
<template>
  <header class="container">
    <div class="logo">
      <h3>Chess Room</h3>
    </div>
    <nav>
      <ul>
        <li><button>Sign Up</button></li>
        <li><button>Login</button></li>
      </ul>
    </nav>
  </header>
</template>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  height: clamp(2rem, 5vw, 3.2rem);
  position: absolute;
  top: 0;
  width: 100%;
}

nav {
  align-content: center;
}

ul {
  list-style: none;
  display: flex;
  gap: 1rem;
}
ul li {
  display: inline-block;
}

.logo h3 {
  font-size: clamp(1.25rem, 2.25vw, 2.5rem);
}
</style>
