from flask import request
from flask_socketio import emit

from laserfocus.utils.logger import logger

def deploy_main_routes(socketio):
    
    @socketio.on('connect')
    def handle_connect():
        client_id = request.sid
        ip_address = request.remote_addr

        logger.announcement(f"Client {client_id} attempting connection", 'info')
        logger.info(f"IP address: {ip_address}")

        try:
            emit('connected', client_id, broadcast=True)
            logger.announcement(f"Client {client_id} connected", 'success')
        except Exception as e:
            logger.error(f"Error connecting client {client_id}: {str(e)}")
            emit('error', str(e), to=client_id)

    @socketio.on('disconnect')
    def handle_disconnect():
        client_id = request.sid
        logger.announcement(f"Client {client_id} disconnecting...", 'info')
        try:
            emit('disconnected', client_id, broadcast=True)
            logger.announcement(f"Client {client_id} disconnected", 'info')
        except Exception as e:
            logger.error(f"Error disconnecting client {client_id}: {str(e)}")