from app.tests.base_test_case import BaseTestCase
from http import HTTPStatus

class ClientTestCase(BaseTestCase):

    def test_create_and_get_client(self):
        create_response = self.client.post('/clients', json={
            'name': 'Luiza Labs',
            'email': 'luiza@labs.com'
        })
        self.assertEqual(create_response.status_code, HTTPStatus.CREATED)
        self.assertIn(b'Client created successfully', create_response.data)

        get_response = self.client.get('/clients/luiza@labs.com')
        self.assertEqual(get_response.status_code, HTTPStatus.OK)
        self.assertIn(b'Luiza Labs', get_response.data)
        self.assertIn(b'luiza@labs.com', get_response.data)

    def test_update_client(self):
        self.client.post('/clients', json={
            'name': 'Magazine',
            'email': 'magazine@mag.com'
        })

        update_response = self.client.put('/clients/magazine@mag.com', json={
            'email': 'magazinelabs@mag.com',
            'name': 'Magazine Labs'
        })
        self.assertEqual(update_response.status_code, HTTPStatus.OK)
        self.assertIn(b'Client updated successfully', update_response.data)

        get_response = self.client.get('/clients/magazine@mag.com')
        self.assertEqual(get_response.status_code, HTTPStatus.OK)
        self.assertIn(b'Magazine Labs', get_response.data)

    def test_delete_client(self):
        self.client.post('/clients', json={
            'name': 'Laboratório',
            'email': 'laboratorio@lab.com'
        })

        delete_response = self.client.delete('/clients/laboratorio@lab.com')
        self.assertEqual(delete_response.status_code, HTTPStatus.OK)
        self.assertIn(b'Client deleted successfully', delete_response.data)

        get_response = self.client.get('/clients/laboratorio@lab.com')
        self.assertEqual(get_response.status_code, HTTPStatus.NOT_FOUND)
