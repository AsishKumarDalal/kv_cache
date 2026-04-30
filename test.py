import torch
import torch.nn as nn


class Modelcfg:
    n_t_layers=1
    n_heads=1
    d_model=128
    vocab=50000
    conext_size=256

class SelfAttention(nn.Module):
    def __init__(self,d_model,d_out):
        self.w_q=nn.Linear(d_model,d_out)
        self.w_k=nn.Linear(d_model,d_out)
        self.w_v=nn.Linear(d_model,d_out)
    def forward(self,x):
        q=self.w_q(x)
        k=self.w_k(x)
        v=self.w_v(x)
        attn_scores=q@k.T
        t = attn_scores.size(0)
        mask = torch.tril(torch.ones(t, t))
        attn_scores=attn_scores.masked_fill(mask==0,float("-inf")) #casual masking
        attn_mat=torch.softmax(attn_scores,dim=-1)
        return attn_mat@v
    
class MultiHeadAttention(nn.Module):
    def __init__(self,d_model,n_heads):
        d_heads=d_model//n_heads
        self.attention=nn.ModuleList(
            [
                SelfAttention(d_model,d_heads) for _ in range(n_heads)
            ]
        )
    def forward(self,x):
        temp=[head(x) for head in self.attention]
        return torch.cat(temp,-1)
    

class FeedForward(nn.Module):
    def __init__(self,d_model):
        self.l1=nn.Linear(d_model,d_model*4)
        self.l2=nn.Linear(d_model*4,d_model)
    def forward(self,x):
        x=self.l1(x)
        x=nn.ReLU(x)
        x=self.l2(x)
        x=nn.ReLU(x)
        return x

class TransFormer(nn.Module):

    def __init__(self,d_model,n_heads):
        self.norm1=nn.RMSNorm(d_model)
        self.norm2=nn.RMSNorm(d_model)
        self.attn=MultiHeadAttention(d_model,n_heads)
        self.ff=FeedForward(d_model)

    def forward(self,x):
        temp=x
        x=self.norm1(x)
        x=self.attn(x)
        temp=temp+x
        x=self.norm2(temp)
        x=self.ff(x)
        return temp+x

class SLM(nn.Module):
    def __init__(self,cfg:Modelcfg):
        self.val_embed=nn.Embedding(cfg.vocab,cfg.d_model)
        self.pos_embed=nn.Embedding(cfg.conext_size,cfg.d_model)
        self.tflayers=nn.ModuleList([TransFormer(cfg.d_model,cfg.n_heads)for _ in range(cfg.n_t_layers)])
        self.fnorm=nn.RMSNorm(cfg.d_model)
        self.out_head=nn.Linear(cfg.d_model,cfg.vocab)

    def forward(self,x):
        v_embed=self.val_embed(x)















