import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from team_project2 import client
db = client.team_project2
from flask import request, redirect, url_for, jsonify, Blueprint
from datetime import datetime
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from .auth1 import get_user


model = tf.keras.models.load_model('team_project2/static/model/model3.h5')

bp = Blueprint('file',__name__)

@bp.route('/fileupload', methods=['POST'])
def file_upload():
    file = request.files['file_give']
    extension = file.filename.split('.')[-1]
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'{mytime}'
    save_to = f'team_project2/static/img/catdog/{filename}.{extension}'
    file.save(save_to)
    return jsonify({'result': 'success'})

@bp.route('/result')
def result():
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    test_dir = 'team_project2/static/img'
    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(64, 64),
        color_mode="rgb",
        shuffle=False,
        class_mode=None,
        batch_size=1)
    pred = model.predict(test_generator)
    user = get_user()
    # 강아지
    if pred[-1] > 0.5:
        db.user.update_one({'email':user['email']},{'$set':{'face':'dog'}})
        return redirect(url_for('main.dog'))
    # 고양이
    else:
        db.user.update_one({'email': user['email']}, {'$set': {'face': 'cat'}})
        return redirect(url_for('main.cat'))
