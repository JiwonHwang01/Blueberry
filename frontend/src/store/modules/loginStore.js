import axios from 'axios'
import router from '../../router'

const loginStore = {
    state: {
        token: localStorage.getItem('token') || '',
        refreshToken: localStorage.getItem('refreshToken') || '',
        user: null,
        isLogin: false,
    },
    mutations: {
      SET_TOKEN(state, token) {
        state.token = token;
        localStorage.setItem('token', token);
      },
      SET_REFRESH_TOKEN(state, refreshToken) {
        state.refreshToken = refreshToken;
        localStorage.setItem('refreshToken', refreshToken);
      },
      SET_USER(state, user) {
        state.user = user;
        state.isLogin = true;
      },
      LOGOUT(state) {
        state.token = '';
        state.refreshToken = '';
        state.user = null;
        localStorage.removeItem('token');
        localStorage.removeItem('refreshToken');
      },
    },
    actions: {
        login ({commit}, loginObj) {
        return axios.post('http://localhost:8000/api/token/', loginObj)
          .then(response => {
            commit('SET_TOKEN', response.data.access);
            commit('SET_REFRESH_TOKEN', response.data.refresh);
            axios.defaults.headers.common.Authorization = `Bearer ${response.data.access}`
            this.dispatch('getMemberInfo') // 유저 정보를 가져오는 actions 호출
            console.log(response.data.access)
          })
        },
        signup(_, signupData) {
            return axios.post('http://localhost:8000/api/auth/signup/', signupData)
            .then(response => {
                if (response.data.success) {
                alert('회원가입이 완료되었습니다.');
                }
                else{
                    console.error('Signup error:', response.data.errors);
                }
            })
            .catch(error => {
                console.error('Signup error:', error);
                alert('회원가입에 실패했습니다.');
            });
        },
        getMemberInfo ({ commit }) { // 토큰으로 유저 정보를 받아오는 코드
          const token = localStorage.getItem('token') // 저장된 access 토큰을 가져옴
          const config = {
            headers: {
              Authorization: 'Bearer ' + token,
            }
          }
          axios
            .get('http://localhost:8000/api/auth/user/', config) 
            .then((response) => {
              const userInfo = {
                pk: response.data.pk,
                username: response.data.username,
                email: response.data.email,
              } // 유저 정보를 받아옴
              commit('SET_USER', userInfo) // mutations 호출
              console.log(response.data.username,' Login !')
              router.push('/home');
            })
            .catch(err => {
                console.log(err);
              alert('이메일과 비밀번호를 확인하세요.')
            })
        },
        refresh({ commit, state }) {
            return axios.post('http://localhost:8000/api/token/refresh/', {
            refresh: state.refreshToken,
            })
            .then(response => {
            commit('SET_TOKEN', response.data.access);
            });
        },
        logout({ commit }) {
            commit('LOGOUT');
        },
    },
    getters: {
      isAuthenticated: state => !!state.token,
      user: state => state.user,
    },
  }

  export default loginStore