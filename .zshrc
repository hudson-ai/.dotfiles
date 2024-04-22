# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Theme
source ~/.zsh/powerlevel10k/powerlevel10k.zsh-theme
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# Plugins
source ~/.zsh/fast-syntax-highlighting/fast-syntax-highlighting.plugin.zsh
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
#source ~/.zsh/zsh-autocomplete/zsh-autocomplete.plugin.zsh

# Env variables and aliases
export SSH_KEY_PATH="~/.ssh/rsa_id"
export PATH="$HOME/.cargo/bin:$PATH"
export PATH="$HOME/.local/share/bob/nvim-bin:$PATH"
export PATH="$HOME/.local/bin/:$PATH"
export PATH="$HOME/bin:$PATH"

if command -v nvim &> /dev/null; then
  alias vim=nvim
fi

if command -v bat &> /dev/null; then
  alias cat=bat
fi

if command -v exa &> /dev/null; then
  alias ls=exa
fi

# Conda
conda_path=$HOME/miniconda3/bin/conda
if command -v $conda_path &> /dev/null; then
  eval "$($conda_path shell.zsh hook)"
fi

# zoxide
if command -v zoxide &> /dev/null; then
  eval "$(zoxide init zsh --cmd cd)"
fi
