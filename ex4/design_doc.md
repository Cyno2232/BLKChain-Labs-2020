# 区块链 LAB4 设计文档

1811459 张倬玮 1811400 吕建瑶

## a. 解释你的代码内容，以及coinExchangeScript是怎么工作的

```python
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    return [
        # fill this in!
        OP_DEPTH, 2, OP_EQUAL, 
        OP_IF, 
        OP_HASH160, hash_of_secret, OP_EQUALVERIFY, public_key_recipient, OP_CHECKSIG, 
        OP_ELSE,
        2, public_key_sender, public_key_recipient, 2, OP_CHECKMULTISIG,
        OP_ENDIF  
    ]

# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    return [
        # fill this in!
        sig_recipient,
        secret
    ]

# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [
        # fill this in!
        OP_0, 
        sig_sender ,
        sig_recipient  
    ]
```

由于需要区别两种不同的情况（接受者赎回交易/交易超时而将硬币退还给发送者），coinExchangeScript 函数用到了 if/else 操作符区别这两种情况。

* 首先通过脚本长度区分两个脚本
* 其次处理情况1：**OP_HASH160, hash_of_secret, OP_EQUALVERIFY **将栈中的 secret 进行哈希运算，与公开的 Hash(x) 比较，检验秘密 x 是否正确；**public_key_recipient, OP_CHECKSIG** 比对栈中的接受者签名是否正确。
* 否则处理情况2：**2, public_key_sender, public_key_recipient, 2, OP_CHECKMULTISIG** 验证发送者和接受者的两个签名。



## b. 以 Alice 用 coinExchangeScript 向 Bob 发送硬币为例：如果 Bob 不把钱赎回来，Alice 为什么总能拿回她的钱？为什么不能用简单的 1/2 MultiSig 来解决这个问题？

当 Alice 用 coinExchangeScript 向 Bob 发送硬币时，如果 Bob 不履行承诺，Alice 将不会在交易上签名，秘密 x 的值也不会披露，所以Bob 不能拿到 Alice 的币。直到 time-locked transaction 解冻时，Alice 赎回自己的币。

此问题不能用简单的1/2multsig来解决，原因是：如果使用简单的 1/2 multsig，任一方都可以单独打破约定，从而使另一方受损。而使用以上机制可以保证双方的利益一定都不会受损，因为没有任何一方可以单独毁约，不通过对方的配合而赎回硬币。



## c. 解释Alice（Bob）创建的一些交易内容和先后次序，以及背后的设计原理

交易流程：

（1）Alice 创建第一笔交易，指定解锁方式为双方共同签名，或 Bob 的签名加上 Alice 创建的秘密 x.

（2）Alice 创建第二笔交易，指定解锁方式为：在到达指定的解锁时间 locktime 之后，可以赎回自己的币。

此时 Bob 不能索要这笔硬币，因为不知道 Alice 创建的秘密 x；Alice 也不能拿回自己的硬币，因为没有到 locktime.

（3）Bob 创建第一笔交易，指定解锁方式为双方共同签名，或 Alice 的签名加上 Alice 创建的秘密 x.（使用同样的Hash(x)）

（4）Bob 创建第二笔交易，指定解锁方式为：在到达指定的解锁时间 locktime 之后，可以赎回自己的币。

此时 Alice 可以索要 Bob 的硬币，使用其签名和秘密 x 解锁 Bob 的第一笔交易。此时秘密 x 将会被广播到区块链上，从而被 Bob 获取。这时 Bob 也可以解锁 Alice 的第一笔交易，拿回 Alice 的硬币。

如果交易没有达成，双方可以在解锁时间后取回各自的硬币。



## d. 本次作业中，一次成功的跨链原子交换中，资金是如何流转的？

在一次成功的跨链原子交换中，资金的流转方式为：

Alice 生成秘密 x 后，先将自己用于交换的 BTC 锁定在输出脚本中，随后 Bob 使用同样的 Hash(x)，也将自己的 BCY 锁定在输出脚本中。然后 Alice 使用 x 解锁 Bob 的输出脚本，获取 Bob 的 BCY 到自己的钱包中，并且广播 x，Bob 也使用 x 解锁 Alice 的输出脚本，获取 Alice 的 BTC 到自己的钱包中，交易结束。