###############################################################################
#    マイグレーションやORマッピングに使用する共有用メタクラスを生成します。
###############################################################################
from sqlalchemy.ext.declarative.api import declarative_base
Base = declarative_base()

# このパッケージで定義されているモデルをすべてロード
# Alembicにて自動的にマイグレーションを行う
import sys
sys.path.insert(0, "./model")
import toilet, toilet_group, toilet_group_map, toilet_status, app_state
