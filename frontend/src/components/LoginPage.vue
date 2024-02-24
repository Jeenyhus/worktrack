<template>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <div class="card">
            <div class="card-header">Login</div>
            <div class="card-body">
              <form @submit.prevent="login">
                <div class="mb-3">
                  <label for="username" class="form-label">Username</label>
                  <input type="text" id="username" v-model="username" class="form-control" required>
                </div>
                <div class="mb-3">
                  <label for="password" class="form-label">Password</label>
                  <input type="password" id="password" v-model="password" class="form-control" required>
                </div>
                <button type="submit" class="btn btn-primary">Login</button>
              </form>
              <div v-if="error" class="text-danger mt-3">{{ error }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
        error: ''
      };
    },
    methods: {
      async login() {
        try {
          // Replace this with actual authentication logic using an API
          // Example: const response = await axios.post('/api/login', { username: this.username, password: this.password });
          // Then handle the response accordingly (e.g., redirect to dashboard if login successful)
          console.log('Logged in successfully');
        } catch (error) {
          this.error = 'Failed to login. Please check your credentials.';
        }
      }
    }
  };
  </script>
  