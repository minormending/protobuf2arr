# protobuf2arr
 Translate a protobuf message to Google's RPC array format. Many non-public  Google services use an array wire format for protobuf messages where each field number is mapped to an index of an array.

# Example
 The following protobuf message `Message` gets translated to the array: `[field1_value, field2_value]`.
 ```
message Message {
    int32 field1 = 1;
    string field2 = 2;
}
 ```

Python implementation:
 ```
import message_pb2
message = message_pb2.Message()
message.field1 = 77
message.field2 = "Hello World"
 ```

RPC array format:
```
[77, "Hello World"]
```

# Installation and Usage

## Installation

You can install the package directly from github via:
```
pip install git+https://github.com/minormending/protobuf2arr
```

## Usage
Assuming we have a protobuf message format defined as such:
```
syntax = "proto3";

package mypackage;

message TaskQueue {
    int32 queue_id = 1;
    string queue_name = 2;
    repeated TaskItem items = 3;

    message TaskItem {
        int32 task_id = 1;
        string task_name = 2;
        string date = 4; 
    }
}
```

The message is transformed via `protoc` to `taskqueue_pb2.py`. Normal protobuf usage applies to the generated message:
```
import taskqueue_pb2

task_queue = taskqueue_pb2.TaskQueue()
task_queue.queue_id = 78
task_queue.queue_name = "redis:thread:tasks"

for i in range(2):
    task = taskqueue_pb2.TaskQueue.TaskItem()
    task.task_id = i + 1
    task.task_name = f"cleanup:{i + 1}"
    task.date = '2022-04-01'
    task_queue.items.append(task)

print(task_queue)
```

This produces the standardize protobuf string representation:
```
queue_id: 78
queue_name: "redis:thread:tasks"
items {
  task_id: 1
  task_name: "cleanup:1"
  date: "2022-04-01"
}
items {
  task_id: 2
  task_name: "cleanup:2"
  date: "2022-04-01"
}
```

However, when we serialize the protobuf message to an array `serialize(task_queue)`, we get the following:
```
[78, 'redis:thread:tasks', [[1, 'cleanup:1', '2022-04-01'], [2, 'cleanup:2', '2022-04-01']]]
```