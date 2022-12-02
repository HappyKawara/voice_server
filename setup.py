from setuptools import setup

package_name = 'voice_server'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kawara',
    maintainer_email='c1139136@planet.kanazawa-it.ac.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "stt = voice_server.stt_server:main",
            "tts = voice_server.tts_srvserver:main",
            "client_sa = voice_server.client_sample:main",
            "client = voice_server.client_member_function:main",
            "service = voice_server.service_member_function:main",
            "a = voice_server.a:main",
            "cli_tts = voice_server.client_tts:main"
        ],
    },
)
