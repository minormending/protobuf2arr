# protobuf2arr
 Translate a protobuf message to Google's RPC array format. Many non-public  Google services use an array wire format for protobuf messages where each field number is mapped to an index of an array (one-based).

# Simple Example
 The following protobuf message `Message` gets translated to the array: `[field1_value, field2_value]`.
 
 Protobuf implementation:
 ```
syntax = "proto3";

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

## Skipping field numbers 
Since fields are mapped to indexes of an array, missing field numbers are included as `None` or `null` types. 

Let's add a new field `field3` to the protobuf message above, but with a number of `4`, skipping `3`.
```
syntax = "proto3";

message Message {
    int32 field1 = 1;
    string field2 = 2;
    bool field3 = 4;
}
```

Python implementation remains the same, with the addition of enabling `field3`.
```
message.field3 = True
```

RPC array format now includes `None` or `null` (serialized string) for the missing field `3` and the value of `field3` in the array position `4` (one-based). 
```
[77, "Hello World", null, True]
```

# Installation

You can install the package directly from pypi:
```
pip install protobuf2arr
```

# Usage
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

However, when we serialize the protobuf message to an array `serialize_msg2arr(task_queue)`, we get the following:
```
[78, 'redis:thread:tasks', [[1, 'cleanup:1', '2022-04-01'], [2, 'cleanup:2', '2022-04-01']]]
```

# Nullable Types
Consider the empty state for the task queue with a single empty task.
```
task_queue = taskqueue_pb2.TaskQueue()
task_queue.items.append(taskqueue_pb2.TaskQueue.TaskItem())
serialize_msg2arr(task_queue)
```
```
[0, '', [[0, '', '']]]
```
Protobuf fields empty state is their type default, so `0` for `int32` and the empty string for `string`. However, many Google api's require `None` or `null` for field empty states. 

This library allows you to include a `nullable` option on any field where the default value should be translated to a `None` type. The `nullable` custom option can be included either of two ways in your protobuf schema, the serializer only cares about the option name.

## Inline declaration
Declare the custom option inline in your proto file:
```
import "google/protobuf/descriptor.proto";

extend google.protobuf.FieldOptions {
    optional string nullable = 50027;
}
```
The option extension number does not matter, so long as it is within the proper Protobuf field option range. Now you to tag your fields with this option and the specific value (`string`) you want to be parsed to `None` as such:
```
int32 queue_id = 1 [(nullable) = '0'];
```

## Package declaration
Alteratively, you can define this custom option in a separate proto file and import it into your message.

nullable_option.proto:
```
syntax = "proto3";

package protobuf2arr;

import "google/protobuf/descriptor.proto";

extend google.protobuf.FieldOptions {
    optional string nullable = 50027;
}
```

message.proto:
```
syntax = "proto3";

package mypackage;

import "nullable_option.proto"

message TaskQueue {
    int32 queue_id = 1 [(nullable_option.nullable) = '0'];
}
```

## Output
Assume that we want to ignore the `queue_name` and `date` fields and send the `None` or `null` type when they are not set, we can use protobuf custom field options. Regardless of which method is choosen, we get the results:

message.py:
```
task_queue = taskqueue_pb2.TaskQueue()
task_queue.items.append(taskqueue_pb2.TaskQueue.TaskItem())
serialize_msg2arr(task_queue)
```
output:
```
[null, '', [[0, '', null]]]
```

# Nullable Messages
Set the `nullable` tag to the empty message state `''` to support lists of messages where an item is `None` i.e the default state. Alternatively, more complicated default states are supported:

message.proto:
```
repeated TaskItem items = 3 [(nullable) = 'task_id: 1'];
```

message.py:
```
task_queue = taskqueue_pb2.TaskQueue()
task = taskqueue_pb2.TaskQueue.TaskItem()
task.task_id = 1
task_queue.items.append(task)
serialize_msg2arr(task_queue)
```

output:
```
[null, '', [null]]
```