import http from 'k6/http';
import { sleep, check } from 'k6';

// Конфігурація для 3 типів навантаження
export const options = {
    stages: [
        { duration: '1m', target: 20 }, // Load Test: поступовий підйом до 20 користувачів
        { duration: '1m', target: 100 }, // Stress Test: різкий підйом до 100, щоб знайти межу
        { duration: '1m', target: 20 }, // Soak Test: тривале стабільне навантаження
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'], // 95% запитів мають бути швидше за 500мс
    },
};

export default function () {
    const res = http.get('http://localhost:8000/api/test');
    check(res, {
        'status is 200': (r) => r.status === 200,
        'protocol is HTTP/1.1': (r) => r.proto === 'HTTP/1.1',
    });
    sleep(1);
}