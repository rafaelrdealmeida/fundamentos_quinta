# Mini-curso - Fundamentos de Análise de dados

Mini-curso - Fundamentos de **Análise de dados**


## Preparação do ambiente de trabalho

### Versionamento

- GITHUB e GITLAB: rede social para compatilhar código
- GIT: versionar o código
- [OhShitGit](https://ohshitgit.com/pt_br/swears/)

#### Versionando o código
  
  ```
  git add .
  ```

  ```
  git commit -m "inserir mensagem aqui"
  ```

#### Sincronizar o repositório local com o remoto

  ```
  git pull orign main
  ```

  ```
  git push orign main
  ```

### Comandos básicos linux

```
ls
cd
cd..
mkdir
history
cat
touch
rm -r caminho/do arquivos
cp caminho_origem caminho_destino
mv caminho_origem caminho_destino

```

### Editor de Código

- `VScode`
- Google Colab

## Ambiente Virtual

- Software utilizado para a gestão do ambiente: `conda`

```
conda env create -f environment.yml 
```

```
conda activate nome_ambiente
```

```
conda env update
```