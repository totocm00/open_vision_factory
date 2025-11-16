import os, sys, subprocess, importlib

REQ_FILE = "requirements_test.txt"
TARGET_PKG = "tensorflow"

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

def find_pkg_line(pkg_name: str):
    with open(REQ_FILE) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.lower().startswith(pkg_name):
                return line
    return None

def ensure_tensorflow():
    try:
        import tensorflow as tf
        print(f"[INFO] TensorFlow already installed ({tf.__version__})")
        return tf, False
    except ImportError:
        pkg_line = find_pkg_line("tensorflow")
        if not pkg_line:
            raise RuntimeError("tensorflow not found in requirements_test.txt")
        print("### 텐서플로 설치중... (Installing TensorFlow...) ###")
        subprocess.run([sys.executable, "-m", "pip", "install", pkg_line], check=True)
        tf = importlib.import_module("tensorflow")
        return tf, True

def uninstall_tensorflow():
    print("### 텐서플로 삭제중... (Uninstalling TensorFlow...) ###")
    for name in ("tensorflow", "tensorflow-cpu", "tensorflow-gpu"):
        subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", name], check=False)
    print("[CLEANUP] TensorFlow removed.")

def main():
    tf, installed_here = ensure_tensorflow()
    from tensorflow import keras
    from tensorflow.keras import layers

    gpus = tf.config.list_physical_devices("GPU")
    print("[TF] GPUs:", gpus)
    if gpus:
        for gpu in gpus:
            try:
                tf.config.experimental.set_memory_growth(gpu, True)
            except Exception:
                pass

    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    x_train = (x_train / 255.0).astype("float32")[..., None]
    x_test = (x_test / 255.0).astype("float32")[..., None]

    model = keras.Sequential([
        layers.Conv2D(16, 3, activation="relu", input_shape=(28, 28, 1)),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(64, activation="relu"),
        layers.Dense(10, activation="softmax"),
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    model.fit(x_train, y_train, epochs=1, batch_size=256, verbose=1, validation_data=(x_test, y_test))

    print("[DONE] TensorFlow GPU test finished. (텐서플로 GPU 정상 작동 중 ✅)")

    if installed_here:
        uninstall_tensorflow()

if __name__ == "__main__":
    main()