# FChat_PI_CaseUse
projeto para disciplina de programação para internet
Crie um projeto e implemente usando Django models o seguinte estudo de caso:
a.	Um usuário tem um ou mais perfis numa rede social;
b.	Um perfil tem uma timeline;
c.	Um perfil possui vários contatos como relacionamento;
d.	Uma timeline pode ter várias postagens;
e.	Uma postagem pode ter vários comentários;
f.	Um comentário tem um perfil associado;
g.	Uma postagem pode ter várias reações.
h.	Uma reação possui um tipo: curtir, amar, rir, se impressionar, ficar triste ou se irritar;
i.	Um perfil pode reagir a postagens, porém cada reação pode ter um peso. Ex: 10 curtidas. Assim, há a necessidade de um contador/peso na associação.
__
Demais atributos:
–	Usuário: id, email, senha, data de nascimento;
–	Perfil: 	nome e usuario;
–	Postagem: texto, data e perfil;
–	Comentario: texto, data, perfil e postagem;
–	Reacao: tipo, data, postagem, perfil e peso.

Insira registros em cada uma das tabelas pelo shell e envie o link do projeto em um repositório como resposta da atividade.
