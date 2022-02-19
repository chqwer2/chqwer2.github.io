### RoBERTa-LR

RoBERTa基本架构上使用线性递增的学习率

```python

def create_optimizer(model,adjust_task_specific_lr=False):
    named_parameters = list(model.named_parameters())    
    
    roberta_parameters = named_parameters[:388]    
    attention_parameters = named_parameters[388:392]
    regressor_parameters = named_parameters[392:]
        
    attention_group = [params for (name, params) in attention_parameters]
    regressor_group = [params for (name, params) in regressor_parameters]

    parameters = []

    if adjust_task_specific_lr:
      for layer_num, (name, params) in enumerate(attention_parameters):
        weight_decay = 0.0 if "bias" in name else 0.01
        parameters.append({"params": params,
                           "weight_decay": weight_decay,
                           "lr": Config.task_specific_lr})
      for layer_num, (name, params) in enumerate(regressor_parameters):
        weight_decay = 0.0 if "bias" in name else 0.01
        parameters.append({"params": params,
                           "weight_decay": weight_decay,
                           "lr": Config.task_specific_lr})   
    else:
      parameters.append({"params": attention_group})
      parameters.append({"params": regressor_group})
    
    increase_lr_every_k_layer = 1
    lrs = np.linspace(1, 5, 24 // increase_lr_every_k_layer)
    for layer_num, (name, params) in enumerate(roberta_parameters):
        weight_decay = 0.0 if "bias" in name else 0.01
        splitted_name = name.split('.')
        lr = Config.lr
        if len(splitted_name) >= 4 and str.isdigit(splitted_name[3]):
            layer_num = int(splitted_name[3])
            lr = lrs[layer_num // increase_lr_every_k_layer] * Config.lr 

        parameters.append({"params": params,
                           "weight_decay": weight_decay,
                           "lr": lr})

    return AdamW(parameters)
```



### Attention Head with multi-layer

```
class AttentionHead(nn.Module):
    def __init__(self, h_size, hidden_dim=512):
        super().__init__()
        self.W = nn.Linear(h_size, hidden_dim)
        self.V = nn.Linear(hidden_dim, 1)
        
    def forward(self, features):
        att = torch.tanh(self.W(features))
        score = self.V(att)
        attention_weights = torch.softmax(score, dim=1)
        context_vector = attention_weights * features
        context_vector = torch.sum(context_vector, dim=1)

        return context_vector

class CLRPModel(nn.Module):
    def __init__(self,transformer,config):
        super(CLRPModel,self).__init__()
        self.h_size = config.hidden_size
        self.transformer = transformer
        self.head = AttentionHead(self.h_size*4)
        self.linear = nn.Linear(self.h_size*2, 1)
        self.linear_out = nn.Linear(self.h_size*8, 1)

              
    def forward(self, input_ids, attention_mask):
        transformer_out = self.transformer(input_ids, attention_mask)
       
        all_hidden_states = torch.stack(transformer_out.hidden_states)
        cat_over_last_layers = torch.cat(
            (all_hidden_states[-1], all_hidden_states[-2], all_hidden_states[-3], all_hidden_states[-4]),-1
        )
        
        cls_pooling = cat_over_last_layers[:, 0]   
        head_logits = self.head(cat_over_last_layers)
        y_hat = self.linear_out(torch.cat([head_logits, cls_pooling], -1))
        
        return y_hat
```

