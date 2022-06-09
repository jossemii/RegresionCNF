# celaut
python3 -m grpc_tools.protoc -I. --python_out=. celaut.proto --experimental_allow_proto3_optional &&
# onnx
python3 -m grpc_tools.protoc -I. --python_out=. onnx.proto --experimental_allow_proto3_optional &&
# regresion
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. regresion.proto --experimental_allow_proto3_optional &&
# solvers_dataset
python3 -m grpc_tools.protoc -I. --python_out=. solvers_dataset.proto --experimental_allow_proto3_optional

# Pyarmor
pyarmor obfuscate start.py
mv dist .service