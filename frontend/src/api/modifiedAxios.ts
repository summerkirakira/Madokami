import axios from 'axios';
import { useUserStore } from '@/stores/user'
import pinia from '../stores'


const userStore = useUserStore(pinia);

const globalAxios = axios.create({
    baseURL: 'http://localhost:8000'
});

globalAxios.interceptors.request.use(
    response => {
        return response;
    },
    error => {
        if (error.response.status === 404) {
            userStore.logout();
            window.location.href = '/login';
        }
        return Promise.reject(error);
    }
);

export default globalAxios;
