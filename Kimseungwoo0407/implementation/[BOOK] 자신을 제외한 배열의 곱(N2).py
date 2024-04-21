outputs = [1,2,3,4]

result = [0] * len(outputs)

for i in range(len(outputs)):
    outputs_mul = 1
    if i == 0:
        for output in outputs[1:]:
            outputs_mul *= output
        result[i] = outputs_mul
    elif i == len(outputs)-1:
        for output in outputs[:len(outputs)-1]:
            outputs_mul *= output
        result[i] = outputs_mul
    else:
        for output in outputs[:i]:
            outputs_mul *= output
        for output in outputs[i+1:]:
            outputs_mul *= output
        result[i] = outputs_mul

print(result)